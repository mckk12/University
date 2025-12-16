using UnityEngine.SceneManagement;
using UnityEngine;

public class Menu : MonoBehaviour
{
    void Start()
    {
        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;
    }
    public void StartNormal()
    {
        Debug.Log("Starting game...");
        SceneManager.LoadScene("ShootingRange");
    }

    public void StartSwarm()
    {
        Debug.Log("Starting swarm mode...");
        SceneManager.LoadScene("SwarmMode");
    }

    public void QuitGame()
    {
        Application.Quit();
    }
}
