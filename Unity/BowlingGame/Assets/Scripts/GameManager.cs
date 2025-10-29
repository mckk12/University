using System;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{

    public Text scoreText;
    public GameObject pinsParent;
    public GameObject ball;
    private Vector3 originalBallPosition;
    private Vector3[] originalPinsPosition;
    private Quaternion[] originalPinsRotation;

    public bool resetting = false;
    

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
        if (Input.GetKeyDown(KeyCode.Space))
        {
            ResetLane();
            resetting = true;
        }
        if (ball.transform.position.x > -45f)
        {
            resetting = false;
        }
        if (ball.transform.position.y < -15f)
        {
            CountScore();
        }
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            SceneManager.LoadScene("MenuScene");
        }
    }
    
    void FixedUpdate()
    {
        if (resetting)
        {
            for (int i = 0; i < pinsParent.transform.childCount; i++)
            {
                Transform pin = pinsParent.transform.GetChild(i);
                pin.transform.position = Vector3.Lerp(pin.position, originalPinsPosition[i], 0.2f);
                pin.transform.rotation = Quaternion.Slerp(pin.rotation, originalPinsRotation[i], 0.2f);
                pin.GetComponent<Rigidbody>().linearVelocity = Vector3.zero;
                pin.GetComponent<Rigidbody>().angularVelocity = Vector3.zero;
            }

        }
    }

    public void CountScore()
    {
        int CurrentScore = 0;
        foreach (Transform child in pinsParent.transform)
        {
            // Debug.Log((1f/180f) + "Pin info: " + child.name + " Rot x: " + child.rotation.x + " Rot z: " + child.rotation.z + " Rot y: " + child.rotation.y);
            if (Math.Abs(child.rotation.x) > (1f / 150f)
                || Math.Abs(child.rotation.z) > (1f / 150f))
            {
                CurrentScore += 1;
            }
        }
        scoreText.text = CurrentScore==10 ? "Strike!" : CurrentScore.ToString();  
    }

    public void ResetLane()
    {
        Debug.Log("Resetting ball and pins...");
        ball.transform.position = originalBallPosition;
        ball.GetComponent<Rigidbody>().linearVelocity = Vector3.zero;
        ball.GetComponent<Rigidbody>().angularVelocity = Vector3.zero;
        scoreText.text = "0";
    }
}
