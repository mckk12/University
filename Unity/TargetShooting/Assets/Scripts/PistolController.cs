using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.UI;

public class PistolController : MonoBehaviour
{
    public Transform pistolTransform;
    public Vector3 aimingPosition = new(0f, -1.43f, 9.4f);
    public Vector3 hipPosition = new (1.4f, -2.9f, 9.4f);
    public Animation animations;

    public AudioSource shootAudioSource;
    public AudioSource reloadAudioSource;
    public AudioSource emptyMagAudioSource;

    public GameObject bulletPrefab;

    public Text ammoDisplay;
    public Text reloadPrompt;
    public int maxAmmo = 12;
    private int currentAmmo = 12;

    [Header("Input actions")]
    public InputActionReference shootAction;
    public InputActionReference reloadAction;
    public InputActionReference aimAction;

    private bool aimingOn = false;
    private bool reloading = false;

    void OnDisable()
    {
        reloadPrompt.enabled = false;
        if (reloading)
        {
            currentAmmo = 0;
            reloading = false;
            animations.Stop("Reload");
            reloadAudioSource.Stop();
        }
        
    }

    void OnEnable()
    {
        animations.Play("PickUpPistol");
        // currentAmmo = maxAmmo;
        ammoDisplay.text = currentAmmo.ToString();
        // reloadPrompt.enabled = false;
        aimingOn = false;
        reloading = false;
    }

    void Start()
    {
        currentAmmo = maxAmmo;
        ammoDisplay.text = currentAmmo.ToString();
        reloadPrompt.enabled = false;
    }

    void FixedUpdate()
    {
        if (aimingOn){
            pistolTransform.localPosition = Vector3.Slerp(pistolTransform.localPosition, aimingPosition, 0.3f);
        }
        else if (!aimingOn){
            pistolTransform.localPosition = Vector3.Slerp(pistolTransform.localPosition, hipPosition, 0.3f);
        }

    }

    void Update()
    {
        if (aimAction.action.WasPerformedThisFrame())
        {
            aimingOn = !aimingOn;
        }
    

        if (shootAction.action.WasPerformedThisFrame() && currentAmmo > 0 && !reloading)
        {           
                ShootPistol();
        }

        if (currentAmmo == 0)
        {
            reloadPrompt.enabled = true;
            if (shootAction.action.WasPerformedThisFrame() && !reloading)
            {
                animations.Stop("OutOfAmmo");
                animations.Play("OutOfAmmo");
                emptyMagAudioSource.Play();
            }
        }

        if (reloadAction.action.WasPerformedThisFrame() && currentAmmo < maxAmmo && !reloading)
        {

            currentAmmo = 0;
            animations.Play("Reload");
            reloadAudioSource.Play();
            reloading = true;

        }
        ammoDisplay.text = currentAmmo.ToString();
    }

    void ShootPistol()
    {
        animations.Stop("Shoot");
        animations.Play("Shoot");
        shootAudioSource.Play();
        currentAmmo--;
        GameObject bullet = Instantiate(bulletPrefab, pistolTransform.position + pistolTransform.forward * -3f + pistolTransform.up * 1.1f, pistolTransform.rotation * Quaternion.Euler(0f, 180f, 0f));
        bullet.GetComponent<Rigidbody>().linearVelocity = pistolTransform.forward * 500f;
    }

    void ReloadPistol()
    {
        reloadPrompt.enabled = false;
        currentAmmo = maxAmmo;
        reloading = false;
    }
}
