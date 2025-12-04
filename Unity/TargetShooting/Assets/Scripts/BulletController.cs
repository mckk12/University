using UnityEngine;

public class BulletController : MonoBehaviour
{
    public float bulletSpeed = 50f;
    public float lifeTime = 2f;

    public AudioSource lampHitSound;

    void Update()
    {
        lifeTime -= Time.deltaTime;
        if (lifeTime <= 0f)
        {
            Destroy(gameObject);
        }
    }

    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.CompareTag("Lamp"))
        {
            lampHitSound.Play();
        }
    }
}