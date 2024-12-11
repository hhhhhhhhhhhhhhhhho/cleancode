// 의도를 분명히 밝혀라 

// 의도가 드러나지 않은 변수명

int d; // 경과 시간(단위:날짜)

// 의도가 잘 드러나는 변수명
int elapsedTimeInDays;
int daysSinceCreation;
int daysSinceModifications;
int fileAgeInDayss;


/// 의도가 드러나지 않는 Function

public List<int[]> getThem(){
    List<int[]> list1 = new ArrayList<int[]>();
    for (int[] x: theList)
        if(x[0] == 4) 
            list1.add(x);
    return list1;
}

// 같은 기능이지만 의도가 드러나는 Function
// 지뢰찾기 게임을 만드는 것이라고 생각해보자. theList 가 게임판이라는 사실을 금새 알 수 있다.

public List<int[]> getFlaggedCells(){
    List<int[]> flaggesCells = new ArrayLisit<int[]>();
    for (int[] cell: gameboard)
        if(cell[STATUS_VALUE] == FLAGGED) // 혹은 if(cell.isFlagged()) 로 바꿔도 좋을 것 같다.
            flaggesCells.add(cell);
    return flaggesCells
}