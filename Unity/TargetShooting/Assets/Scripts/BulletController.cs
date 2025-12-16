using UnityEngine;

public class BulletController : MonoBehaviour
{
    public float bulletSpeed = 50f;
    public float lifeTime = 2f;

    public AudioSource lampHitSound;

    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.CompareTag("Lamp"))
        {
            lampHitSound.Play();
        }
        Destroy(gameObject);
    }

    void OnTriggerEnter(Collider other)
    {
        Destroy(gameObject);
    }
}