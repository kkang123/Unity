```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class player_ctr1 : MonoBehaviour {
    private float power;
    public float power_plus = 100.0f;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButton(0))
            power += power_plus * Time.deltaTime;
        if (Input.GetMouseButtonUp(0))
        {
            this.GetComponent<Rigidbody>().AddForce(new Vector3(power, power, 0));
            power = 0.0f; //초기화
        }
        if (this.transform.position.y < -5.0f || Input.GetMouseButtonDown(1)) //포지션 y값이 -0.5 아래로 떨어지면
            SceneManager.LoadScene("main"); //Scene 초기화
    }
}

```