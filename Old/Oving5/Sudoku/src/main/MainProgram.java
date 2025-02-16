package main;

import java.util.ArrayList;
import java.util.HashMap;

import main.Assignment5.CSP;
import main.Assignment5.CSP.Pair;

public class MainProgram {
	
	static ArrayList<String> variables;
	
	static HashMap<String, HashMap<String, ArrayList<Pair<String>>>> constraints;
	
	static int teller = 0;
	static int FailureTeller = 0;
	
	
	public static void main(String[] args) {
		
		System.out.println("");
		CSP sudoko = Assignment5.createSudokuCSP("src/main/veryhard.txt");
		Assignment5.printSudokuSolution(sudoko.backtrackingSearch());
		System.out.println("");
		System.out.println("Level:  easy.txt");
		System.out.println("Number of times your BACKTRACK method was called: " + teller);
		System.out.println("Number of times your BACKTRACK method failed: " + FailureTeller);
		
		
		
	}
}
