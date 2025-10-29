using UnityEngine;

public class BallMovement : MonoBehaviour
{
    public MeshRenderer lane;
    public Rigidbody rb;

    public float spinFactor = 0.05f;

    private int throwFlag = 0;
    private Vector2 mouseStartPos;
    private Vector2 mouseEndPos;
    void Update()
    {
        if (Input.GetMouseButtonDown(0) && throwFlag==0)
        {
            mouseStartPos = Input.mousePosition;
            Debug.Log("Mouse down at: " + mouseStartPos);
            throwFlag = 1;
        }
        else if (Input.GetMouseButtonUp(0) && throwFlag==1)
        {
            mouseEndPos = Input.mousePosition;
            Vector2 throwVector = mouseEndPos - mouseStartPos;
            Debug.Log("Mouse up at: " + mouseEndPos + ", throw vector: " + throwVector);
            rb.linearVelocity = new Vector3(throwVector.y * 0.1f, -1f, -throwVector.x * 0.01f);
            throwFlag = 2;
        }
        if (Input.GetKeyDown(KeyCode.Space))
        {
            throwFlag = 0;
        }
    }

    void FixedUpdate()
    {

        if (throwFlag == 0)
        {
            if (rb == null || Camera.main == null) return;
            Vector3 mouseScreen = Input.mousePosition;

            mouseScreen.z = Camera.main.WorldToScreenPoint(transform.position).z;
            Vector3 worldPos = Camera.main.ScreenToWorldPoint(mouseScreen);

            // clamp z based on lane's Z length (use bounds.extents.z as half-length)
            float laneHalfZ = lane.bounds.extents.z;
            float minZ = lane.bounds.center.z - laneHalfZ;
            float maxZ = lane.bounds.center.z + laneHalfZ;
            float clampedZ = Mathf.Clamp(worldPos.z, minZ, maxZ);

            rb.MovePosition(new Vector3(worldPos.x, rb.position.y, clampedZ));
        }
        if (throwFlag == 2)
        {
            float spin = Input.GetAxis("Mouse X");
            rb.linearVelocity = new Vector3(rb.linearVelocity.x, rb.linearVelocity.y, rb.linearVelocity.z - spin * spinFactor);
        }
    }

}
