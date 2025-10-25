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
            ResetGame(); 
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
                child.hasChanged = false;

            }
        }
        scoreText.text = CurrentScore.ToString();   
    }

    public void ResetGame()
    {
        scoreText.text = "0";
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }

    public void ResetBallPins()
    {
        Debug.Log("Resetting ball and pins...");
        ball.transform.position = originalBallPosition;
        for (int i = 0; i < pinsParent.transform.childCount; i++)
        {
            Transform pin = pinsParent.transform.GetChild(i);
            pin.position = originalPinsPosition[i];
            pin.rotation = originalPinsRotation[i];
        }
    }
}
