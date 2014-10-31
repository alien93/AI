package main;

import java.util.ArrayList;
import java.util.HashMap;

import main.Assignment5.CSP;
import main.Assignment5.CSP.Pair;

public class Hei {
	
	static ArrayList<String> variables;
	
	static HashMap<String, HashMap<String, ArrayList<Pair<String>>>> constraints;
	
	
	public static void main(String[] args) {
		
		CSP sudoko = Assignment5.createSudokuCSP("src/main/veryhard.txt");
		Assignment5.printSudokuSolution(sudoko.backtrackingSearch());
		
	}
}
