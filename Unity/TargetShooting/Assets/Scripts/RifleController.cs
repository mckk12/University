using System.Collections;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.Rendering;
using UnityEngine.Rendering.Universal;
using UnityEngine.UI;

public class RifleController : MonoBehaviour
{
    public Transform rifleTransform;
    public Vector3 aimingPosition = new(0.18f,-6.52f,8.7f);
    public Vector3 hipPosition = new (1.4f,-7.2f,8.7f);
    public Animation animations;

    public AudioSource shootAudioSource;
    public AudioSource reloadAudioSource;
    public AudioSource emptyMagAudioSource;

    public GameObject bulletPrefab;
    public Volume globalVolume;

    public Text ammoDisplay;
    public Text reloadPrompt;
    public int maxAmmo = 30;
    public int currentAmmo = 30;

    private bool aimingOn = false;
    public bool reloading = false;
    public float shotCooldown = 0.1f; // seconds between shots
    private float nextShotTime = 0f;

    [Header("Input actions")]
    public InputActionReference shootAction;
    public InputActionReference reloadAction;
    public InputActionReference aimAction;

    void OnDisable()
    {
        
        if (reloading)
        {
            reloading = false;
            animations.Stop("Reload");
            reloadAudioSource.Stop();
        }
        
    }

    void OnEnable()
    {
        animations.Play("PickUpRifle");
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
            rifleTransform.localPosition = Vector3.Slerp(rifleTransform.localPosition, aimingPosition, 0.3f);
        }
        else if (!aimingOn){
            rifleTransform.localPosition = Vector3.Slerp(rifleTransform.localPosition, hipPosition, 0.3f);
        }

    }

    void Update()
    {
        if (aimAction.action.WasPerformedThisFrame())
        {
            aimingOn = !aimingOn;
        }
    

        if (shootAction.action.IsPressed() && currentAmmo > 0 && !reloading && Time.time >= nextShotTime)
        {           
            
            ShootPistol();
            nextShotTime = Time.time + shotCooldown;
        }

        if (currentAmmo == 0)
        {
            reloadPrompt.enabled = true;
            if (shootAction.action.WasPerformedThisFrame() && !reloading)
            {
                emptyMagAudioSource.Play();
            }
        }

        if (reloadAction.action.WasPerformedThisFrame() && currentAmmo < maxAmmo && !reloading)
        {

            currentAmmo = 0;
            animations.Play("RifleReload");
            reloadAudioSource.Play(); //TODO: add proper reload sound
            reloading = true;

        }
        ammoDisplay.text = currentAmmo.ToString();
    }

    void ShootPistol()
    {
        animations.Stop("RifleShoot");
        animations.Play("RifleShoot");
        shootAudioSource.Play();
        StartCoroutine(ShootFlash());
        currentAmmo--;
        GameObject bullet = Instantiate(bulletPrefab, 
            rifleTransform.position + rifleTransform.forward * -1.7f + rifleTransform.up * 5.5f + rifleTransform.right * 0.1f,
            rifleTransform.rotation);
        bullet.GetComponent<Rigidbody>().linearVelocity = rifleTransform.forward * -800f;
    }

    void ReloadRifle()
    {
        reloadPrompt.enabled = false;
        currentAmmo = maxAmmo;
        reloading = false;
    }

    IEnumerator ShootFlash()
    {
        if (globalVolume.profile.TryGet<ColorAdjustments>(out var ca))
        {
            ca.postExposure.value = 0.5f;
            yield return new WaitForSeconds(0.05f);
            ca.postExposure.value = 0f;
        }
    }
}
