// 87%
function solution(A) {
    let numOfIntersectingDisc = 0;
    const INTERSECTION_LIMIT = 10000000;
    let startEndPairs = A.map((value, i) => [i - value, i + value]);
    
    startEndPairs = startEndPairs.sort((a, b) => a[0] - b[0]);
    
    startEndPairs.some((value, i) => {
        
      for (let j = i + 1; j < A.length; j++) {
        
        if (startEndPairs[j][0] <= startEndPairs[i][1]) {
          numOfIntersectingDisc++;
        } else {
          break;
        }
        if (numOfIntersectingDisc > INTERSECTION_LIMIT) {
          numOfIntersectingDisc = -1;
          break;
        }
      }
      
      return numOfIntersectingDisc > INTERSECTION_LIMIT;
    });
    return numOfIntersectingDisc;
  }
  