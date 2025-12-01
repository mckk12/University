using UnityEngine;

public class PistolController : MonoBehaviour
{
    public GameManager gameManager;
    public Transform pistolTransform;
    public Vector3 aimingPosition = new(0f, -1.43f, 9.4f);
    public Vector3 hipPosition = new (1.4f, -2.9f, 9.4f);
    public Animation animations;

    public AudioSource shootAudioSource;
    public AudioSource reloadAudioSource;
    public AudioSource emptyMagAudioSource;

    public GameObject bulletPrefab;

    private bool aimingOn = false;
    private bool reloading = false;

    void Start()
    {
        
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
        if (Input.GetKeyDown(gameManager.aimKey))
        {
            aimingOn = !aimingOn;
        }
    

        if (Input.GetKeyDown(gameManager.shootKey) && gameManager.currentAmmo > 0 && !reloading)
        {           
                ShootPistol();
        }

        if (gameManager.currentAmmo == 0)
        {
            gameManager.reloadPrompt.enabled = true;
            if (Input.GetKeyDown(gameManager.shootKey) && !reloading)
            {
                animations.Stop("OutOfAmmo");
                animations.Play("OutOfAmmo");
                emptyMagAudioSource.Play();
            }
        }

        if (Input.GetKeyDown(gameManager.reloadKey) && !reloading)
        {

            gameManager.currentAmmo = 0;
            animations.Play("Reload");
            reloadAudioSource.Play();
            reloading = true;

        }
        gameManager.ammoDisplay.text = gameManager.currentAmmo.ToString();
    }

    void ShootPistol()
    {
        animations.Stop("Shoot");
        animations.Play("Shoot");
        shootAudioSource.Play();
        gameManager.currentAmmo--;
        GameObject bullet = Instantiate(bulletPrefab, pistolTransform.position + pistolTransform.forward * -3f + pistolTransform.up * 1.1f, pistolTransform.rotation * Quaternion.Euler(0f, 180f, 0f));
        bullet.GetComponent<Rigidbody>().linearVelocity = pistolTransform.forward * 500f;
        Destroy(bullet, 5f);
    }

    void ReloadPistol()
    {
        gameManager.reloadPrompt.enabled = false;
        gameManager.currentAmmo = gameManager.maxAmmo;
        reloading = false;
    }
}
