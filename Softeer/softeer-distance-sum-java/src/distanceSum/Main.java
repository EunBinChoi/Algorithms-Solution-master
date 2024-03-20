package distanceSum;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Node {
    int num;
    long cost;
    public Node(){}
    public Node(int a,long b){
        num = a;
        cost = b;
    }
	public int getNum() {
		return num;
	}
	public void setNum(int num) {
		this.num = num;
	}
	public long getCost() {
		return cost;
	}
	public void setCost(long cost) {
		this.cost = cost;
	}
	@Override
	public String toString() {
		return "Node [num=" + num + ", cost=" + cost + "]";
	}
}

public class Main {
	public static ArrayList<Node> adj[]; // adjacency list
	public static ArrayList<Integer> subtreeSize;
	public static ArrayList<Long> subtreeDistSum;
	public static int N;
	
	public static void dfs1(int current, int parent) {
		subtreeSize.set(current, 1);
		for(int i = 0; i < adj[current].size(); i++) {
			int child = adj[current].get(i).num;
			long cost = adj[current].get(i).cost;
			
			if(parent != child) { // int compare
				dfs1(child, current); // bottom-up
				subtreeSize.set(current, subtreeSize.get(current) + subtreeSize.get(child));
				subtreeDistSum.set(current, subtreeDistSum.get(current) + subtreeDistSum.get(child) + cost * subtreeSize.get(child));
				
			}
		}
	}
	
	public static void dfs2(int current, int parent) {
		for(int i = 0; i < adj[current].size(); i++) {
			int child = adj[current].get(i).num;
			long cost = adj[current].get(i).cost;
			
			if(parent != child) { // int compare
				subtreeDistSum.set(child, (subtreeDistSum.get(current) + cost * (N - 2*subtreeSize.get(child))));
				dfs2(child, current);
			}
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());

		
		/////////////////////////////////////////////////////////////
		// make graph with adjacency list
		/////////////////////////////////////////////////////////////
		adj = new ArrayList[N + 1]; // 1 ~ N
		subtreeSize = new ArrayList<>(N + 1); // 1 ~ N
		subtreeDistSum = new ArrayList<>(N + 1); // 1 ~ N
		/////////////////////////////////////////////////////////////
		
		
		/////////////////////////////////////////////////////////////
		// initialize the adjacency list, subtreeSize, subtreeDistSum
		/////////////////////////////////////////////////////////////
		adj[0] = null;
		subtreeSize.add(null);
		subtreeDistSum.add(null);
		
		for(int i = 1; i < adj.length; i++){
            adj[i] = new ArrayList<Node>();
            subtreeSize.add(0);
            subtreeDistSum.add(0L);
        }
		////////////////////////////////////////////////////////////
		
		for(int i = 1; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            long c = Integer.parseInt(st.nextToken());
            adj[s].add(new Node(e,c));
            adj[e].add(new Node(s,c));
		}
		
		dfs1(1, 1);
		dfs2(1, 1);
		
		for(int i = 1; i <= N; i++) {
			System.out.println(subtreeDistSum.get(i));
		}
		
	}

}
