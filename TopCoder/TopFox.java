import java.util.ArrayList;
public class TopFox{
	public static void main(String[] args){
		String familyName = new String();
		String givenName = new String();
		if (args.length == 0){
			familyName = "ab";
			givenName = "cd";
		}
		else {
			familyName = args[0];
			givenName = args[1];
		}

		System.out.println(familyName + " " + givenName);
		System.out.println(possibleHandles(familyName, givenName));
	
	}
	public static  int possibleHandles(String familyName, String givenName){
		StringBuffer famPrefix = new StringBuffer();
		StringBuffer givPrefix = new StringBuffer();
		ArrayList<String> handles = new ArrayList<String>();
		int numberHandles = 0;
		for(int i =0 ;i < familyName.length(); i++){
			famPrefix.append(familyName.charAt(i));
			StringBuffer handle = new StringBuffer(famPrefix);
			System.out.println(handle + " is the handle");
			for(int j = 0; j<givenName.length();j++){
				handle.append(givenName.charAt(j));
				String handleWord = new String(handle);
				if (!handles.contains(handleWord)){
					numberHandles++;
					handles.add(handleWord);
					System.out.println(handle);
				}

			}
			
		}
		return numberHandles;	
	}

}
