// 先序
public static void preOreder(Node node) {
   if (node == null)
       return;
   System.out.print(node.data  + " ");
   preOrder(node.left);
   preOrder(node.right);
}
// 中序
public static void inOrder(Node node){
   if (node == null)
       return;
   inOrder(node.left);
   System.out.print(node.data + " ");
   inOrder(node.right);
}
//后序
public void postOrder(Node, node){
   if (node == null)
       return;
   postOrder(node.left);
   postOrder(node.right);
   System.out.print(node.data + " ");
}
