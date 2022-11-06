```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class wall : MonoBehaviour
{
    public float speed = -5; //벽이 오는 속도
    // Start is called before the first frame update
    void Start()
    {
        Destroy(gameObject, 5.0f); //일정 시간 지나면 벽 오브젝트 삭제
    }

    // Update is called once per frame
    void Update()
    {
        transform.Translate(speed * Time.deltaTime, 0, 0);
    }
}

```