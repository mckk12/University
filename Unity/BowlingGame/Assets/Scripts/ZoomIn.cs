using UnityEngine;

public class ZoomIn : MonoBehaviour
{
    public Camera mainCamera;
    public float zoomSpeed = 2f;
    public float targetFOV = 30f;
    private bool shouldZoom = false;
    private float originalFOV;

    void Start()
    {
        if (mainCamera == null)
            mainCamera = Camera.main;
        originalFOV = mainCamera.fieldOfView;
    }

    void OnTriggerEnter(Collider other)
    {
        Debug.Log("Trigger entered by: " + other.name);
        shouldZoom = true;

    }

    void Update()
    {
        if (shouldZoom)
        {
            mainCamera.fieldOfView = Mathf.Lerp(mainCamera.fieldOfView, targetFOV, Time.deltaTime * zoomSpeed);
        }
    }
}
