package ron;

import java.util.*;

public class Graph<T> {
	
	private Map<T, List<T>> map = new HashMap<>();
	
	public void addVertext(T s) {
		this.map.put(s, new LinkedList<T>());
	}
	
	public void addEdge(T source, T dest, boolean bidirectional){
		if(!this.map.containsKey(source))
			addVertext(source);
		if(!this.map.containsKey(dest))
			addVertext(dest);
		this.map.get(source).add(dest);
		if(bidirectional)
			this.map.get(dest).add(source);
	}
	
	public int getVertexCount() {
		return this.map.keySet().size();
	}
	
	public boolean hasVertex(T s) {
		return this.map.containsKey(s);
	}
	
	public boolean hasEdge(T s, T d) {
		return this.map.get(s).contains(d);
	}
	
	public String toString() {
		StringBuilder builder = new StringBuilder();
		
		for(T v : map.keySet()) {
			builder.append(v.toString() + ": " );
			for(T w : map.get(v))
				builder.append(w.toString()+" ");
			builder.append("\n");
		}
		
		return builder.toString();
		
	}
	
	
	
	public void bfs(T start) {
		boolean[] visited = new boolean[this.getVertexCount()];
		LinkedList<T> queue = new LinkedList<>();
		visited[]
	}
	
	public static void main(String args[]) {
		
		Graph<Integer> g = new Graph<>();
		g.addEdge(0, 1, true);
		g.addEdge(0, 4, true);
		g.addEdge(1, 2, true);
		g.addEdge(1, 3, true);
		g.addEdge(1, 4, true);
		g.addEdge(2, 3, true);
		g.addEdge(3, 4, true);
		
		System.out.println(g);
		
    }
}
