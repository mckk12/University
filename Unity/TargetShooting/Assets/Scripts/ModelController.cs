using UnityEngine;

public class ModelController : MonoBehaviour
{
    public GameObject bulletHolePrefab;
    public CapsuleCollider headCollider;
    public AudioSource destroySound;
    public AudioSource hitSound;

    public Transform playerTransform;
    public float moveSpeed = 5f;
    public float rotationSpeed = 360f;
    public float strafeAmplitude = 1f; 
    public float strafeSpeed = 0.5f;   

    public int health = 100;
    public int headShotDamage = 50;
    public int bodyShotDamage = 20;
    public bool isSwarmMode = false;

    private Rigidbody rb;
    private float baseX;
    private float strafeSpeedMul = 1f;
    private float strafeAmpMul = 1f;
    private float strafePhase = 0f;

    void Awake()
    {
        rb = GetComponent<Rigidbody>();
    }

    void Start()
    {
        baseX = transform.position.x;
        // Slightly faster and randomized strafe
        strafeSpeedMul = Random.Range(1.15f, 1.5f);
        strafeAmpMul = Random.Range(0.9f, 1.2f);
        strafePhase = Random.value * Mathf.PI * 2f;
    }

    void OnCollisionEnter(Collision collision)
    {
        Vector3 contactPoint = collision.contacts[0].point;
        Instantiate(bulletHolePrefab, contactPoint + collision.contacts[0].normal * 0.01f, Quaternion.LookRotation(collision.contacts[0].normal) * Quaternion.Euler(0f,180f,0f), transform);
        hitSound.Play();
        
        if (headCollider != null && headCollider.bounds.Contains(contactPoint))
        {
            health -= headShotDamage;
        }else{
            health -= bodyShotDamage;
        }
        
        if (health <= 0)
        {
            Destroy(gameObject);
            destroySound.Play();
        }

    }

    void FixedUpdate()
    {
        if (isSwarmMode ){

            Vector3 toPlayer = playerTransform.position - transform.position;
            Vector3 direction = new(toPlayer.x, 0f, toPlayer.z);
            if (direction.sqrMagnitude < 0.0001f) return;

            direction.Normalize();
            Vector3 nextPos = transform.position + direction * moveSpeed * Time.fixedDeltaTime;
            nextPos.y = transform.position.y; 

            Quaternion targetRot = Quaternion.LookRotation(-direction, Vector3.up);

            if (rb != null)
            {
                rb.MovePosition(nextPos);
                rb.MoveRotation(Quaternion.RotateTowards(transform.rotation, targetRot, rotationSpeed * Time.fixedDeltaTime));
            }
            else
            {
                transform.SetPositionAndRotation(nextPos, Quaternion.RotateTowards(transform.rotation, targetRot, rotationSpeed * Time.fixedDeltaTime));
            }
        } else{
            float time = (Time.time + strafePhase) * strafeSpeed * strafeSpeedMul;
            float offset = Mathf.Sin(time) * (strafeAmplitude * strafeAmpMul);
            Vector3 current = transform.position;
            Vector3 nextPos = new (baseX + offset, current.y, current.z);

            if (rb != null)
            {
                rb.MovePosition(nextPos);
            }
            else
            {
                transform.position = nextPos;
            }
        }
    }


}
