using UnityEngine.SceneManagement;
using UnityEngine;

public class Menu : MonoBehaviour
{
    void Start()
    {
        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;
    }
    public void StartGame()
    {
        Debug.Log("Starting game...");
        SceneManager.LoadScene("ShootingRange");
    }

    public void QuitGame()
    {
        Application.Quit();
    }
}
