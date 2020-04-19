package 진학사;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

//문제 설명
//자연수로 이루어진 배열 numbers가 입력으로 주어집니다. 배열에서 과반수를 차지하는 숫자를 찾아 반환하도록 함수 solution을 완성해 주세요.
//
//만약 과반수를 차지하는 숫자가 없으면 -1을 반환해 주세요. 과반수를 차지하는 원소는 전체 n개의 원소 중 n/2개를 초과하는 원소를 말합니다.
//
//제한사항
//배열의 크기는 1이상 500,000이하의 자연수입니다.
//배열의 원소는 1이상 99이하의 자연수입니다.
//입출력 예
//numbers	result
//[6, 1, 6, 6, 7, 6, 6, 7]	6
//[6, 1, 6, 6, 7, 5, 6, 7]	-1
//입출력 예 설명
//입출력 예 #1
//배열이 [6, 1, 6, 6, 7, 6, 6, 7]이며 전체 8개의 원소 중 5개의 원소가 6으로 과반수를 차지하므로 6을 반환합니다.
//
//입출력 예 #2
//배열이 [6, 1, 6, 6, 7, 5, 6, 7]이며 전체 8개의 원소 중 4개의 원소가 6으로 과반수를 차지하지 않으므로 -1을 반환합니다.

class Solution {
    public int solution(int[] numbers) {
    	
    	Map<Integer, Integer> mapObj = new HashMap<>();
    	
		for(int i=0; i<numbers.length; i++) {
			int number = numbers[i];
			
			if(mapObj.containsKey(number)) {
				mapObj.put(number, mapObj.get(number)+1);
			}else {
				mapObj.put(number, 1);
			}
		}
    	
    	int answer = -1;
    	
    	// 과반수 구하기
    	Double majorityNum = Math.ceil(numbers.length / 2.0);
    	
		for ( Map.Entry<Integer,Integer> entry : mapObj.entrySet() ) {
			
			if(entry.getValue() >= majorityNum) {
				answer = entry.getKey();
			}
		}
    	
        return answer;
    }
}

public class One {
    public static void main(String[] args) throws Exception {
    	BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		
		// String 배열 형태로 받은 문자열 "[", "]" 잘라서 String배열 만들기
		String[] strArray = reader.readLine().trim().replace("[", "").replace("]", "").split(",");
		
		ArrayList<Integer> numberArray = new ArrayList<>();
		
		//String 배열 Trim후 Integer형으로 변환
		for(String str : strArray) {
			numberArray.add(Integer.parseInt(str.trim()));
		}
		
		Map<Integer, Integer> mapObj = new HashMap<>();
		
		for(int i=0; i<numberArray.size(); i++) {
			int number = numberArray.get(i);
			
			if(mapObj.containsKey(number)) {
				mapObj.put(number, mapObj.get(number)+1);
			}else {
				mapObj.put(number, 1);
			}
		}
		
    	int answer = -1;
    	
    	// 과반수 구하기
    	//Double majorityNum = Math.ceil(numberArray.size() / 2.0);
    	int majorityNum = (numberArray.size()/ 2)+1;
    	
		for ( Map.Entry<Integer,Integer> entry : mapObj.entrySet() ) {
			
			if(entry.getValue() >= majorityNum) {
				answer = entry.getKey();
			}
		}
    	
        System.out.println(answer);
		
    }
}
