using UnityEngine;

public class ModelController : MonoBehaviour
{
    public GameObject bulletHolePrefab;
    public CapsuleCollider headCollider;

    public int health = 100;
    public int headShotDamage = 50;
    public int bodyShotDamage = 20;

    void OnCollisionEnter(Collision collision)
    {
        Destroy(collision.gameObject);
        Vector3 contactPoint = collision.contacts[0].point;
        Instantiate(bulletHolePrefab, contactPoint + collision.contacts[0].normal * 0.01f, Quaternion.LookRotation(collision.contacts[0].normal) * Quaternion.Euler(0f,180f,0f), transform);
        if (headCollider != null && headCollider.bounds.Contains(contactPoint))
        {
            health -= headShotDamage;
        }else{
            health -= bodyShotDamage;
        }
        
        if (health <= 0)
        {
            Destroy(gameObject);
        }

    }


}
