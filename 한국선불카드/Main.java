package 한국선불카드;

// 예쁜 단어 만들기 제출 완료
//  2초25점
//   문제의 입력값은 각 언어의 표준입력(stdin) 함수를, 출력값은 표준출력(stdout) 함수를 사용해주세요.
//  어느 작은 섬 나라에 살던 소수 민족 짜이짜이족은 많은 국가의 선진화 지원을 받고 있다. 어느 날 짜이짜이족은 알파벳을 공식 문자로 지정하고, 기존의 영어를 많이 수용하여 새로운 언어를 도입하기로 결정했다. 다른 국가들과 어휘의 공감대를 형성하기 위해 대부분의 영단어를 그대로 사용하기로 결정하였으나, 일부 기존 짜이짜이족 사람들이 적응하기 어려운 단어들은 변형하기로 결정하였다.

//  주민들을 대상으로 진행된 조사결과 짜이짜이족은 영어 모음 a, e, i, o, u가 두 번 이상 연속되는 경우에 발음과 암기에 어려움을 느끼는 것으로 밝혀졌다. 가능한한 기존의 어휘를 최대한 유지하기 위해서 전문가들은 기존의 단어에서 연속된 모음들만을 수정하기로 결정했다. 두 번 이상의 모음이 연속해서 반복되는 경우, 가장 앞의 모음을 제외하고는 생략하여 새로운 단어를 만드는 것이다.

//  예를 들어서 기존의 단어 nooooooryuck은 noryuck로 대체되어 사용된다. 물론 서로 다른 모음이 이어진 것도 모음의 반복으로 보고 ouya는 oya로 대체된다.

//  기존의 영어 단어가 주어질 때, 짜이짜이족이 사용할 수 있는 단어로 변환하는 함수를 완성하시오. 모든 영단어는 알파벳 소문자로만 구성되어 있다. 단어의 길이는 500글자를 넘지 않는다.


// 입/출력 예시
// ⋇ 입출력 형식을 잘 지켜주세요.
// ␣ : 공백
// ↵ : 줄바꿈
// −⇥ : 탭
// 보기 입력 1
// 1
// q
// 출력 1
// q

// 보기 입력 2
// 4
// f
// ioee
// j
// o
// 출력 2
// f
// i
// j
// o

// 보기 입력 3
// 9
// fmjr
// ooaaiee
// miginv
// oeexoaax
// xul
// aieuei
// lyvkxgqpe
// o
// j
// 출력 3
// fmjr
// o
// miginv
// oxox
// xul
// a
// lyvkxgqpe
// o
// j

// 보기 입력 4
// 16
// p
// eeaaxaxu
// chxmtltwsnodtrxt
// eio
// f
// xuaoexuoe
// efhmip
// auuuau
// zizdqn
// oxiaeouea
// gwuyhbxd
// xauoxxeoxxo
// l
// aie
// dzlksxjmt
// axxeauixuux
// 출력 4
// p
// exaxu
// chxmtltwsnodtrxt
// e
// f
// xuxu
// efhmip
// a
// zizdqn
// oxi
// gwuyhbxd
// xaxxexxo
// l
// a
// dzlksxjmt
// axxexux

// 보기 입력 5
// 36
// vstaozpqjqkpde
// ixouaueioioaaexiaxuiauaooaiooooiaixo
// cgktysmracxkdsraqwy
// exeooouaueaoexioiaiioeaeaexixx
// qujzlikg
// aaauoooxiiooeoe
// fispkplbtolrprdxunzlupidvaq
// uieoeoeoiaeuxoxoxxeixeoaaeexoixi
// tactaxjcurcsc
// eoxeeaoiexaixuxooexaiaei
// bclwefpfsiupmvsn
// aaeuoiieeoiiaiaoauueu
// toyimimgyg
// oeeuuiu
// ueryhrtgimgsywxbuyv
// xex
// hsixflqcyrrqltwqbhrgnjgo
// ueaoe
// xurjovqstgzhotalqiqofvou
// oeixuuxexiauo
// eerzgkkmqgbv
// eaxeooeieoeeaxaioaux
// nncbspddfqnzevkqpznxi
// oiaxiooxxoxoauiaioiaieoxxxiaxueauee
// bsvzxghhz
// oaxoaxi
// jcnldqrzykiopywkyhyy
// exeoexxuaaexxooauouxouaxoieiueaxai
// rzldvxugykspafjduwb
// ixuouaoxxauxaauaouoeaauoeixoeaea
// vobvotufjtfjr
// uxuiaioaiaaaxoexiax
// qzoflalnngbuuywulnufi
// uxeauoxoaiuxuxaxuaxouxuaxaoa
// koeiywwwxtdqichlrpxeydryksyoab
// xeexxuoouuuaueeueaiaiexeuiaxo
// 출력 5
// vstazpqjqkpde
// ixoxixuxo
// cgktysmracxkdsraqwy
// exexixixx
// qujzlikg
// axi
// fispkplbtolrprdxunzlupidvaq
// uxoxoxxexexoxi
// tactaxjcurcsc
// exexaxuxoxa
// bclwefpfsipmvsn
// a
// toyimimgyg
// o
// uryhrtgimgsywxbuyv
// xex
// hsixflqcyrrqltwqbhrgnjgo
// u
// xurjovqstgzhotalqiqofvo
// oxuxexi
// erzgkkmqgbv
// exexax
// nncbspddfqnzevkqpznxi
// oxixxoxoxxxixu
// bsvzxghhz
// oxoxi
// jcnldqrzykipywkyhyy
// exexxuxxoxoxoxa
// rzldvxugykspafjduwb
// ixuxxaxaxo
// vobvotufjtfjr
// uxuxoxix
// qzoflalnngbuywulnufi
// uxexoxuxaxuxoxuxa
// koywwwxtdqichlrpxeydryksyob
// xexxuxexo

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(reader.readLine().trim());
		String input, output;
		for(int i=0; i<n; i++) {
			input = reader.readLine().trim();
			
			output = Main.stringBeautify(input);
			
			writer.write(output + "\n");
		}
		
		writer.flush();
		writer.close();
		reader.close();
	}
	
	public static String stringBeautify(String input) {
		// 모음 배열
		String[] vowelArray = {"a", "e", "i", "o", "u"};
		
		// Input 배열
		String[] inputArray = input.split("");
		
		// 결과값
		String resultStr = "";
		
		for(int i = 0; i<inputArray.length; i++) {
			// 해당 문자 모음 인지 체크
			boolean isVowel = Arrays.asList(vowelArray).contains(inputArray[i]);
			
			// 모음이 아니면 문자열 삽입
			if(!isVowel) {
				resultStr += inputArray[i];
			}else {
				
				// 모음이지만 첫번째 문자가 아닌경우
				if(i!=0) {
					// 바로 직전 문자가 모음 인지 체크
					isVowel = Arrays.asList(vowelArray).contains(inputArray[i-1]);
					
					// 모음이 아니면 문자열 삽입
					if(!isVowel) {
						resultStr += inputArray[i];
					}
				}else {
					// 모음이지만 첫번째 문자인 경우 문자열 삽입
					resultStr += inputArray[i];
				}
			}
		}
		
		return resultStr;
		
	}
}
