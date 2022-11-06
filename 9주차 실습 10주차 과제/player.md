```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using UnityEngine.SceneManagement;

public class player : MonoBehaviour
{
    public float jupmp_power = 5;
    //public float jupmp_power = 50; //[edit] - [project setting] - [phyisic]에서 gravity 평균 중력 y값이 -9.8인데 이를 -50으로 설정

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetButtonDown("Jump"))
            GetComponent<Rigidbody>().velocity = new Vector3(0, jupmp_power, 0);
    }


    void OnCollisionEnter(Collision other)
    {
        SceneManager.LoadScene("main_scene");
    }
}

```