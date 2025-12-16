using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.UI;

public class PlayerController : MonoBehaviour
{
    public GameObject primaryWeapon;
    public GameObject secondaryWeapon;
    public Transform playerTransform;    
    public CharacterController controller;
    public Text healthDisplay;
    public float gameSensitivity = 100f;

    public float playerSpeed = 15.0f;
    public float sprintMultiplier = 2f;
    public float jumpHeight = 1.5f;
    private readonly float gravityValue = 15f;

    public int health = 100;


    private Vector3 playerVelocity;
    private bool groundedPlayer;

    

    private float targetPitch = 0f;
    private float targetYaw = 0f;
    private float pitchVel = 0f;
    private float yawVel = 0f;
    public float smoothTime = 0.05f;

    public float recoilNoiseAmount = 1f;
    
    [Header("Health Drain")]
    public float healthDrainInterval = 1f;
    private float healthDrainTimer = 0f;

    [Header("Audio Sources")]
    public AudioSource footstepSound;
    public AudioSource runningSound;

    [Header("Input Actions")]
    public InputActionReference shootAction;
    public InputActionReference moveAction;
    public InputActionReference sprintAction;
    public InputActionReference jumpAction;
    public InputActionReference lookAction;
    public InputActionReference primaryWeaponAction;
    public InputActionReference secondaryWeaponAction;


    private void OnEnable()
    {
        moveAction.action.Enable();
        jumpAction.action.Enable();
        shootAction.action.Enable();
        lookAction.action.Enable();
        sprintAction.action.Enable();
        primaryWeaponAction.action.Enable();
        secondaryWeaponAction.action.Enable();

    }

    private void OnDisable()
    {
        moveAction.action.Disable();
        jumpAction.action.Disable();
        shootAction.action.Disable();
        lookAction.action.Disable();
        sprintAction.action.Disable();
        primaryWeaponAction.action.Disable();
        secondaryWeaponAction.action.Disable();
    }


    void OnTriggerStay(Collider other)
    {
        if (other.gameObject.CompareTag("Model"))
        {
            healthDrainTimer += Time.deltaTime;
            if (healthDrainTimer >= healthDrainInterval)
            {
                health = Mathf.Max(0, health - 2);
                healthDrainTimer -= healthDrainInterval;
            }
        }
    }

    void Start()
    {
        playerTransform.eulerAngles = Vector3.zero;
        if (healthDisplay!=null) healthDisplay.text = health.ToString();
    }
    void Update()
    {
        if (!Application.isFocused) return;

        // Look
        Vector2 lookInput = lookAction.action.ReadValue<Vector2>();
        targetYaw += lookInput.x * gameSensitivity * Time.deltaTime;
        targetPitch -= lookInput.y * gameSensitivity * Time.deltaTime;
        targetPitch = Mathf.Clamp(targetPitch, -89f, 89f);
        float smoothPitch = Mathf.SmoothDampAngle(playerTransform.eulerAngles.x, targetPitch, ref pitchVel, smoothTime);
        float smoothYaw = Mathf.SmoothDampAngle(playerTransform.eulerAngles.y, targetYaw, ref yawVel, smoothTime);
        playerTransform.eulerAngles = new Vector3(smoothPitch, smoothYaw, 0f);

        //Recoil for rifle
        RifleController rc = primaryWeapon.GetComponentInChildren<RifleController>();
        if (shootAction.action.IsPressed() && primaryWeapon.activeSelf && rc.reloading == false && rc.currentAmmo > 0)
        {
            targetPitch -= 0.3f;
            targetYaw += Random.Range(-recoilNoiseAmount / 2f, recoilNoiseAmount / 2f);
        }

        
        // Movement
        groundedPlayer = controller.isGrounded;
        if (groundedPlayer)
        {
            if (playerVelocity.y < -3f)
            playerVelocity.y = -3f;
        }

        Vector2 input = moveAction.action.ReadValue<Vector2>();
        Vector3 inputMove = new(input.x, 0, input.y);
        inputMove = Vector3.ClampMagnitude(inputMove, 1f);

        Vector3 move = Quaternion.Euler(0f, playerTransform.eulerAngles.y, 0f) * inputMove;

        if (groundedPlayer && jumpAction.action.WasPressedThisFrame())
        {
            playerVelocity.y = Mathf.Sqrt(jumpHeight * gravityValue);
        }

        playerVelocity.y -= gravityValue * Time.deltaTime;

        if (sprintAction.action.IsPressed())
        {
            move *= sprintMultiplier;
        }
        Vector3 finalMove = move * playerSpeed + Vector3.up * playerVelocity.y;
        controller.Move(finalMove * Time.deltaTime);

        if (footstepSound != null)
        {
            if (move.x != 0f || move.z != 0f)
            {
                if (!footstepSound.isPlaying && groundedPlayer && !sprintAction.action.IsPressed())
                {
                    runningSound.Pause();
                    footstepSound.Play();
                }
                else if (sprintAction.action.IsPressed() && !runningSound.isPlaying && groundedPlayer)
                {
                    footstepSound.Pause();
                    runningSound.Play();
                }
            }else
            {
                footstepSound.Pause();
                runningSound.Pause();
            }
        }

        // Switch Weapons
        if (primaryWeaponAction.action.WasPerformedThisFrame())
        {
            primaryWeapon.SetActive(true);
            secondaryWeapon.SetActive(false);
        }
        if (secondaryWeaponAction.action.WasPerformedThisFrame())
        {
            primaryWeapon.SetActive(false);
            secondaryWeapon.SetActive(true);
        }

        if (healthDisplay!=null) {
            healthDisplay.text = health.ToString();
        }

        if (health <= 0)
        {
            UnityEngine.SceneManagement.SceneManager.LoadScene("SwarmGameOver");
        }
    }
}
