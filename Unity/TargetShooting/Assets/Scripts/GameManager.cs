using UnityEngine;
using UnityEngine.UI;

public class GameManager : MonoBehaviour
{
    public Text KillCountText;
    private int killCount = 0;

    public Camera mainCamera;
    public BoxCollider floorToSpawnOn;
    public GameObject[] modelPrefabs;
    public GameObject modelsParent;
    public AudioSource destroyModelSound;

    public KeyCode shootKey = KeyCode.Mouse0;
    public KeyCode reloadKey = KeyCode.R;
    public KeyCode aimKey = KeyCode.Mouse1;
    public KeyCode backToMenuKey = KeyCode.Escape;


    public Text ammoDisplay;
    public Text reloadPrompt;
    public int maxAmmo = 12;
    public int currentAmmo;

    public int maxModelsOnScreen = 5;
    
    void Start()
    {
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
        currentAmmo = maxAmmo;
        ammoDisplay.text = currentAmmo.ToString();
        reloadPrompt.text = $"Reload! [{reloadKey}]";
        killCount -= maxModelsOnScreen;
    }

    void FixedUpdate()
    {
        if (modelsParent.transform.childCount < maxModelsOnScreen)
        {
            Vector3 center = floorToSpawnOn.bounds.center;
            Vector3 extents = floorToSpawnOn.bounds.extents;
            float margin = 1f;
            Vector3 spawnPosition = new(
                center.x + Random.Range(-extents.x + margin, extents.x - margin),
                floorToSpawnOn.bounds.max.y + 0.1f,
                center.z + Random.Range(-extents.z + margin, extents.z - margin)
            );


            Vector3 dirToCam = mainCamera.transform.position - spawnPosition;
            dirToCam.y = 0f;
            Quaternion spawnRotation = dirToCam.sqrMagnitude > 0.0001f ? Quaternion.Euler(0f, 180f, 0f) * Quaternion.LookRotation(dirToCam) : Quaternion.identity;


            int randomIndex = Random.Range(0, modelPrefabs.Length);
            GameObject newModel = Instantiate(modelPrefabs[randomIndex], spawnPosition, spawnRotation, modelsParent.transform);
            newModel.GetComponent<ModelController>().destroySound = destroyModelSound;
            killCount++;
        }
    }

    void Update()
    {
        KillCountText.text = Mathf.Max(killCount, 0).ToString();
        if (Input.GetKeyDown(backToMenuKey))
        {
            UnityEngine.SceneManagement.SceneManager.LoadScene("MenuScene");
        }
    }
}
