package 한국선불카드;

// 비밀번호 추정하기 제출 완료
//  2초50점
//   문제의 입력값은 각 언어의 표준입력(stdin) 함수를, 출력값은 표준출력(stdout) 함수를 사용해주세요.
//  대부분의 온라인 서비스는 사용자의 ID와 패스워드를 이용한 인증 방식을 채택하고 있다. 서비스의 제공자와 이용자 모두 가장 간단하게 보안을 제공할 수 있는 수단이기 때문이다. 하지만 수 많은 서비스에서 패스워드 방식의 인증 방식을 사용하기 때문에 한 사용자의 입장에서는 모든 서비스마다 다른 패스워드를 사용할 수 는 없는 실정이다.

//  그렇기에 같은 암호를 많은 서비스에서 똑같거나 비슷하게 활용하는 사용자가 많으며, 그 말은 비교를 통해 사용자의 암호를 추정하거나 여러 서비스에 대한 계정을 동시에 해킹하기 쉽다는 말이 된다.

//  초보적인 해커 동이는 키로깅과 엿보기 등 수 많은 방법을 동원해 모 서비스의 암호에 대한 힌트를 얻을 수 있었다. 하지만 아직 완벽하게 암호를 알아낸 것은 아니므로 이후에는 컴퓨터의 계산 능력을 이용해 추정하고자 한다. 동이가 얻어 낸 힌트들은 패스워드 후보를 좁히기에 유익한 정보였지만, 최적화에 서툰 동이가 짠 프로그램으로는 도저히 제 시간에 암호 후보들을 계산할 수가 없었다.

//  동이가 얻어 낸 정보는 암호의 길이와 암호의 일부분에 대한 정보, 그리고 암호에 포함될 수 있는 후보 단어의 집합이다. 예를 들어서 알파벳 소문자로만 구성되는 15글자의 암호에 대한 일부 정보 a??l?ban???????를 알고 있다고 하자. 이 때 ?는 알 수 없는 알파벳 하나를 나타낸다.

//  그리고 동이가 알아 낸 암호에 포함될 수 있는 6개의 후보 단어가 apple, cow, farmer, banana, bananas, pies라고 하자. 동이가 아는 정보는 이 단어들 중 일부가 원본 패스워드에 포함되어 있다는 점이다. 그러므로 동이가 알아 낸 패스워드 패턴을 위반하지 않으면서 이 단어를 이용해 현재 알 수 없는 나머지 자리를 추정해야 한다. 주어지지 않은 단어를 이용해 ?를 추정하는 것은 너무 경우의 수가 많으므로 하지 않는다.

//  위에 주어진 예시에서는 applebananapies, applebananascow 등으로 패스워드를 추정 가능하다. 동이는 이렇게 주어진 패턴과 후보 단어로 만들 수 있는 패스워드들을 기억하기 쉽도록 사전순으로 시도해보려고 한다. 위의 예시에서는 정답은 applebananapies이 된다.

//  그렇다면 동이가 알아 낸 패스워드 패턴을 위반하지 않으면서 주어진 후보 단어들을 이용해 만들 수 있는 패스워드 후보들 중 사전순으로 가장 빠른 후보를 계산하는 프로그램을 작성해주자.



// 입력 형식
// 첫 줄에는 두 자연수 N과 M이 차례로 주어진다.

// N은 동이가 알아 낸 패스워드 패턴의 길이를 나타내는 1,000이하의 자연수이다.
// M은 패스워드에 포함될 수 있는 단어 후보의 수를 나타내는 1,000이하의 자연수이다.
// 두 번째 줄에는 동이가 알아낸 패스워드 패턴이 알파벳 소문자와 ?로 구성된 N글자의 문자열로 주어진다.

// 이후 총 M줄에 걸쳐서 한 줄에 하나 씩 패스워드에 포함될 수 있는 후보 단어가 주어진다.

// 모든 후보 단어는 20글자 이하의 알파벳 소문자로 구성되어 있다.


// 출력 형식
//  동이가 찾아 낸 패스워드 패턴과 주어진 단어들을 이용해 만들어 낼 수 있는 암호들 중 가장 사전순으로 빠른 것을 출력한다.


// 입/출력 예시
// ⋇ 입출력 형식을 잘 지켜주세요.
// ␣ : 공백
// ↵ : 줄바꿈
// −⇥ : 탭
// 보기 입력 1
// 15 6
// a??l?ban???????
// apple
// cow
// farmer
// banana
// bananas
// pies
// 출력 1
// applebananapies

// 보기 입력 2
// 40 40
// z????dgrktn?x??z?t?h?fki?nbef?t??hf?j?xe
// iuzdtthbfkiznbefh
// rktnlxiuzdtthbfki
// t
// nbefhtukhfdj
// ktnlxiuzdtthbfkiznbe
// dtth
// htukhfdjg
// dj
// bfkiznbefh
// fd
// hbfk
// tnlxiuzdtthbfkiznbef
// znbefhtukhfdjg
// ugjedgrktnlxi
// thbfkiznbef
// fdjgxe
// e
// befh
// x
// grktnlxiuzdtthbfkizn
// e
// nlxiuzdtthbfkiznbe
// jedgrktnlxi
// uzdtth
// uk
// gjedg
// jgxe
// htuk
// g
// xiuzdtthbfkizn
// jedgrktnlxiuzdtthbf
// zn
// x
// xi
// gjedgrktnlxiu
// uzdtth
// iz
// zdtthbfkiznbefht
// jgxe
// efhtukh
// 출력 2
// zndjfdgrktnlxiuzdtthbfkienbefhtukhfdjexe

// 보기 입력 3
// 90 90
// ?dyqa?k?????jq?n?sqj?xkn??q?m??cgj??lv?r?u??h?vwwxes?qgw??t???w???z?w?fn?etg?dyi???iiwp?oh
// xesqqgwhhtxjmwkjyzpw
// znbsqjoxknrbqkmwj
// jmwkjyzpwtfnjetg
// uzlvfriukbhbvww
// uzlvfriukbhbvwwxes
// qkmwjcgj
// jqznbsqj
// fkjqznbsqjoxk
// wtfnjetgmdyiywhiiwpg
// bhbvww
// htxjmwkjyzpwtfnjet
// lvfri
// mdyiywhiiw
// kjyzpwtfnjetgmdyiywh
// qalkxqrf
// wpgoh
// iwpg
// whiiwpgoh
// iywhiiwpg
// qqgwhhtxjmwkjy
// bsqjoxk
// h
// cgjuzlvfriukbhbvww
// wtfnjetgmdy
// zpwtfnjetgmdyiywh
// sqqgwhhtxjmwkjyz
// vfriu
// hhtxjmwkjyz
// jqznbsqjoxknr
// uzlvfriukbh
// vf
// zlvfriukbhbvww
// y
// gmd
// tgmdyiy
// jmwkj
// goh
// njetgmdyiywhiiwp
// gwhhtxjmw
// gjuzlvfr
// qgwhhtxjmw
// dyqalkx
// o
// nbsqjoxknrbqkmwj
// wh
// wkjyzpwtfnjetgmdy
// mwjcgjuz
// esqqgwhhtxjmwkjyz
// hhtxjmwkjyz
// vfriukbhbvwwxesqqg
// f
// bqkmwjcgjuzlvf
// wwxesqqgwh
// fk
// zlvfri
// pwtfnjet
// etgmdyiywhiiwpg
// alkxqrfkjqznbs
// vfr
// alkxqr
// c
// sqqgwhhtxjmwkjyzp
// esqqgwhhtxjmwkjyzpw
// xesqqgwhhtxjmw
// cgjuzlvfriukbhbvww
// ywhi
// kxqrfkjqznbsq
// wjcgjuzlvfriu
// tgmdyiywhiiwp
// wwxesqq
// wh
// lkxqrfkjqzn
// o
// iuk
// qalkxqrfk
// kxqrfkj
// nrbq
// nb
// fn
// friukbhbvwwxesqqgwhh
// go
// nrbq
// bhbvww
// xesqq
// friukbhbvw
// wxes
// 출력 3
// cdyqalkxccccjqznbsqjoxknrcqkmwjcgjczlvfriukbhbvwwxesqqgwhhtxjmwkjyzpwcfnbetgmdyiywhiiwpgoh

/* package 구문을 넣으면 안됩니다 */
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

/* [Notice for Java]
 * - 기본 제공되는 뼈대 코드는 입출력의 이해를 돕기위해 제공되었습니다.
 * - 뼈대코드의 활용은 선택사항이며 코드를 직접 작성하여도 무관합니다.
 * 
 * - 별도의 병렬 처리나 시스템콜, 네트워크/파일접근 등을 하지 마세요 
 * - 입출력의 양이 많은 문제는 BufferedReader와 BufferedWriter를 사용하면 시간을 단축할 수 있습니다.
 * - 클래스 이름은 항상 Main이어야 합니다. 주의하세요.
 * - 모든 입력과 출력은 System.in과 System.out 스트림을 이용해야 합니다.
 */

public class Main3{

    //표준입력을 수행할 Scanner를 선언한다 
    public static Scanner scanner = new Scanner(System.in);

    public static String[] wordArray;

    public static void main(String[] args) throws Exception
    {   //프로그램의 시작부 
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] input = reader.readLine().trim().split(" ");
		
		int wordRange = Integer.parseInt(input[0]);
		
		int wordCount = Integer.parseInt(input[1]);
		
		String pw = reader.readLine().trim();
		
		String[] pwArray = pw.split("");
				
		String resultPw = "";
		
		wordArray = new String[wordCount];
		
		for(int i=0; i<wordCount; i++) {
			wordArray[i] = reader.readLine().trim();
		}
		
		Arrays.sort(wordArray);
		
		System.out.println("wordRange : "+wordRange);
		System.out.println("wordCount : "+wordCount);
		System.out.println("pw        : "+pw);
		System.out.println("pwArray   : "+Arrays.toString(pwArray));
		System.out.println("wordArray : "+Arrays.toString(wordArray));
		
		for(String word : pwArray) {
			resultPw += word;
		}
    	
		System.out.println("결과 : " +resultPw);
		
		for(int i=0; i<pwArray.length; i++) {
			String word = pwArray[i];
			
			matchWord(word).sort(Comparator.naturalOrder());
			
			System.out.println(matchWord(word));
		}
		
    }
    
    public static List matchWord(String word) {
    	List resultList = new ArrayList<>();
    	
    	for(int i=0; i<wordArray.length; i++) {
			if(wordArray[i].contains(word)) {
				resultList.add(wordArray[i]);
			}
    	}
    	
    	return resultList;
    }
    
    //1번 : applebananapies
    //2번 : zndjfdgrktnlxiuzdtthbfkienbefhtukhfdjexe
    //3번 : cdyqalkxccccjqznbsqjoxknrcqkmwjcgjczlvfriukbhbvwwxesqqgwhhtxjmwkjyzpwcfnbetgmdyiywhiiwpgoh

}