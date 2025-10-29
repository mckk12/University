using UnityEngine;

public class LaneManager : MonoBehaviour
{
    public GameObject pinsParent;
    public GameObject ball;
    private Vector3 originalBallPosition;
    private Vector3[] originalPinsPosition;
    private Quaternion[] originalPinsRotation;

    private bool ballStart = true;
    
    private bool resetting = false;
    private Vector3 ballCurrentPosition;

    void Start()
    {
        originalBallPosition = ball.transform.position;
        originalPinsPosition = new Vector3[pinsParent.transform.childCount];
        originalPinsRotation = new Quaternion[pinsParent.transform.childCount];
        for (int i = 0; i < pinsParent.transform.childCount; i++)
        {
            Transform pin = pinsParent.transform.GetChild(i);
            originalPinsPosition[i] = pin.position;
            originalPinsRotation[i] = pin.rotation;
        }
    }

    void Update()
    {
        if (ball.transform.position.y < -10f)
        {
            ResetLane();
            resetting = true;
        }
        if (ball.transform.position.x > -45f)
        {
            resetting = false;
        }

    }

    void FixedUpdate()
    {
        if (ballStart)
        {
            ball.GetComponent<Rigidbody>().linearVelocity = new Vector3(Random.Range(10f, 50f), 0f, Random.Range(-1f, 1f));
            ballStart = false;
        }
        if (resetting)
        {
            resetting = false;
            for (int i = 0; i < pinsParent.transform.childCount; i++)
            {
                Transform pin = pinsParent.transform.GetChild(i);
                pin.transform.position = Vector3.Lerp(pin.position, originalPinsPosition[i], 0.1f);
                pin.transform.rotation = Quaternion.Slerp(pin.rotation, originalPinsRotation[i], 0.1f);
                pin.GetComponent<Rigidbody>().linearVelocity = Vector3.zero;
                pin.GetComponent<Rigidbody>().angularVelocity = Vector3.zero;
                if (pin.transform.position != originalPinsPosition[i] &&
                    pin.transform.rotation != originalPinsRotation[i])
                {
                    resetting = true;
                }
            }
            ballStart = true;

        }
    }

    public void ResetLane()
    {
        Debug.Log("Resetting ball and pins...");
        ball.transform.position = originalBallPosition;
        ball.GetComponent<Rigidbody>().linearVelocity = Vector3.zero;
        ball.GetComponent<Rigidbody>().angularVelocity = Vector3.zero;
    }
}


