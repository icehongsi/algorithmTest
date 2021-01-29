package test;

public class binaryTree {
	public class Node {
		private int data;
		private Node left;
		private Node right;
		
		public Node(int data) {
			this.setData(data);
			setLeft(null);
			setRight(null);
		}
		
		public int getData() {
			return data;
		}
		
		public void setData(int data) {
			this.data = data;
		}
		
		public void setLeft(Node left) {
			this.left = left;
		}
		
		public void setRight(Node right) {
			this.right = right;
		}
		
		public Node getLeft() {
			return this.left;
		}
		
		public Node getRight() {
			return this.right;
		}
		
		
	}
	
	public Node root;
	public binaryTree() {
		this.root = null;
	}
	
	public boolean find(int id) {
		Node current = root;
		while (current != null) {
			if (current.getData() > id) { // id���� Ŭ ��� �����ʿ� ����
				current = current.getRight();
			}
			else if (current.getData() < id) {
				current = current.getLeft();
			}
			else
				return true;
		}
		
		return false;
	}
	
	public boolean delete(int id) {
		Node before = null;
		Node current = root;
		boolean isRightNode = false;
		
		while (current != null) {
			if (current.getData() > id) { // id���� Ŭ ��� �����ʿ� ����
				before = current;
				current = current.getRight();
				isRightNode = true;
			}
			else if (current.getData() < id) {
				before = current;
				current = current.getLeft();
				isRightNode = false;
			}
			else if (current.getData() == id)
				break;
		}
		
		if (current == null)
			return false;
		
		if (current.getLeft() == null && current.getRight() == null) {
			if (isRightNode)
				before.setRight(null);
			else
				before.setLeft(null);
			
		}
		
		else if (current.getLeft() == null) {// �����ʿ��� �ڽ� ��尡 ���� ���
			if (isRightNode)
				before.setRight(current.getRight());
			else
				before.setLeft(current.getRight());			
		}
		
		else if (current.getRight() == null) {
			if (isRightNode)
				before.setRight(current.getLeft());
			else
				before.setLeft(current.getLeft());
		}
		
		else { // �ڽĳ�尡 �� �� ���� ���
			Node leftmost = current.getRight();
			while (leftmost.getLeft() != null) // L ��带 ������ �� �ִ� ��ġ�� Ž��
				leftmost = leftmost.getLeft();
			leftmost.setLeft(current.getLeft()); // L ��� ����
			
			if (isRightNode)
				before.setRight(current.getRight());
			else
				before.setLeft(current.getLeft());
					
		}
		
		return true;		
	}

}
