using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public Transform playerTransform;
    public float gameSensitivity = 10f;
    void Start()
    {
        playerTransform.eulerAngles = Vector3.zero;
    }

    // smoothing targets/velocities
    private float targetPitch = 0f;
    private float targetYaw = 0f;
    private float pitchVel = 0f;
    private float yawVel = 0f;
    public float smoothTime = 0.05f;

    void Update()
    {
        if (!Application.isFocused) return;

        float mouseX = Input.GetAxis("Mouse X") * gameSensitivity * Time.deltaTime * 100f;
        float mouseY = Input.GetAxis("Mouse Y") * gameSensitivity * Time.deltaTime * 100f;

        targetYaw += mouseX;
        targetPitch -= mouseY;
        if (targetPitch > 180f) targetPitch -= 360f; 
        targetPitch = Mathf.Clamp(targetPitch, -80f, 80f);

        float currentPitch = playerTransform.eulerAngles.x;
        float currentYaw = playerTransform.eulerAngles.y;

        float smoothPitch = Mathf.SmoothDampAngle(currentPitch, targetPitch, ref pitchVel, smoothTime);
        float smoothYaw  = Mathf.SmoothDampAngle(currentYaw,  targetYaw,  ref yawVel,  smoothTime);

        playerTransform.rotation = Quaternion.Euler(smoothPitch, smoothYaw, 0f);
    }
}
