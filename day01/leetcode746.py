
def solution(arr):
  start = arr[0]

  if(len(arr) >= 2):
    end = arr[1]
  for i in range(2, len(arr)):
    arr[i] += min(start, end)
    start = end 
    end = arr[i]
  return min(start, end)

if __name__ == "__main__":
  arr = [10 , 15, 20 ]
  print(solution(arr))
