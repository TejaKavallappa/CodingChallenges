public class MatchMakingTest{
	public static void main(String[] args){
		String[] namesWomen = {"Constance", "Bertha", "alice"};
		String[] answersWomen = {"aaba", "baab", "aaaa"};
		String[] namesMen = {"Chip", "Biff", "Abe"};
		String[] answersMen = {"bbaa", "baaa", "aaab"};
		String queryWoman = "Bertha";
		MatchMaking pairing = new MatchMaking();	
		String answer = pairing.makeMatch(namesWomen,answersWomen,namesMen,answersMen,queryWoman);	
		System.out.println(queryWoman + " is matched with "+ answer);
	}
}
