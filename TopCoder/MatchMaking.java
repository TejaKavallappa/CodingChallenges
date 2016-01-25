import java.util.Arrays;
public class MatchMaking{

	public String makeMatch(String[] namesWomen, String[] answersWomen, String[] namesMen, String[] answersMen, String queryWoman){
		if ((namesWomen.length!=answersWomen.length) || (namesMen.length!=answersMen.length) || (namesWomen.length!=namesMen.length))
			throw new IllegalArgumentException("The lengths of the inputs do not match");
		//Initialize array of objects (male and female candidates)		
		int length = namesWomen.length;
		Candidate[] women = new Candidate[length];
		for (int i=0; i<length; i++){
			women[i] = new Candidate(namesWomen[i],answersWomen[i]);	
		}

		Candidate[] men = new Candidate[length];
		for (int i=0; i<length; i++){
			men[i] = new Candidate(namesMen[i],answersMen[i]);		
		}

		Arrays.sort(women);
		Arrays.sort(men);
		for(int w = 0; w<women.length;w++){
			Candidate matchedMan = null;
			int maxScore = -1;
			for (Candidate man : men){
				if (man.answers == null){
					continue;
				}
				int score = getScore(women[w].answers, man.answers);
				if (score>maxScore){
					maxScore = score;
					matchedMan = man;
				}
			}
			matchedMan.answers = null;
			if(women[w].name.equals(queryWoman)){
				return matchedMan.name;
			}


		}

			return new String("No match found");


	}
	private int getScore(String wAnswer,String mAnswer){
		int score = 0;
		for(int i =0;i<wAnswer.length();i++){
			if (wAnswer.charAt(i) == mAnswer.charAt(i))
				score++;		
		}
		return score;
	}
	
}
class Candidate implements Comparable<Candidate>{
	String name;
	String answers;
	Candidate(String name, String answers){
		this.name = name;
		this.answers = answers;
	}
	public int compareTo(Candidate other){
		return this.name.compareTo(other.name);
	}

}


