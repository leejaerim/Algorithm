### timedelta 사용해서 시간사이 분 계산하기

- 시간만큼 문자열을 정리해서 -> `date`간 시간을 계산합니다.
```python
    time_1 = timedelta(hours= int(sh) , minutes=int(sm))
    time_2 = timedelta(hours= int(eh), minutes=int(em))
    return int((time_2 - time_1).seconds/60)
```

- 그 시간길이당 (1분당 1코드) 뮤직코드를 반복 생성합니다.
  - target check.
- C인지 C#인지 체크여부 필요합니다.
  - `replace`사용해서 C#을 c로 치환해서 계산합니다.
    - `replace`없이 알고리즘으로 구현하려고 했으나, 복잡.
    - `C, C#, D, D#, E, F, F#, G, G#, A, A#, B`
- 같은 뮤직이 있을 경우, 더 긴 랭스로 출력해야 합니다. -> `heappush`
  - `heappush(ans,(-length, title))` 큰값의 타이틀을 저장합니다.