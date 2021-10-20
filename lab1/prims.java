import java.util.*;

public class prims{
    public static void main(String[] args) {

    }
}

class Vertex{
    String label;
    Vertex(String label){
        this.label=label;
    }
}

class Graph{
    private Map<Vertex, List<Vertex>> adjVertices; 
}

void addVertex(String label){
    adjVertices.putIfAbsent(new Vertex(label), new ArrayList<>());
}