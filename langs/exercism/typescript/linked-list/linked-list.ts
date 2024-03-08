class Node<T> {
  public value: T | null;
  public prev: Node<T> | null;
  public next: Node<T> | null;

  constructor(
    value: T | null = null,
    prev: Node<T> | null = null,
    next: Node<T> | null = null
  ) {
    this.value = value;
    this.prev = prev;
    this.next = next;
  }
}

export class LinkedList<T> {
  private head: Node<T> | null;
  private length: number;

  constructor() {
    this.head = null;
    this.length = 0;
  }

  public push(element: T): void {
    const newNode = new Node(element);
    if (!this.head) {
      this.head = newNode;
    } else {
      let current = this.head;
      while (current.next) current = current.next;
      current.next = newNode;
      newNode.prev = current;
    }
    this.length++;
  }

  public pop(): T | null {
    if (!this.head) {
      return null;
    } else {
      let current = this.head;
      while (current.next) current = current.next;

      const value = current.value;
      if (current.prev) {
        current.prev.next = null;
      } else {
        this.head = null;
      }
      this.length--;
      return value;
    }
  }

  public shift(): T | null {
    if (!this.head) {
      return null;
    } else {
      const value = this.head.value;
      this.head = this.head.next;
      if (this.head) this.head.prev = null;
      this.length--;
      return value;
    }
  }

  public unshift(element: T): void {
    const newNode = new Node(element, null, this.head);
    if (this.head) {
      this.head.prev = newNode;
    }
    this.head = newNode;
    this.length++;
  }

  public delete(element: T): void {
    if (!this.head) return;

    if (this.head.value === element) {
      this.head = this.head.next;
      if (this.head) this.head.prev = null;
      this.length--;
      return;
    }

    let current: Node<T> | null = this.head;
    while (current) {
      if (current.value === element) {
        if (current.prev) current.prev.next = current.next;
        if (current.next) current.next.prev = current.prev;
        this.length--;
        return;
      }
      current = current.next;
    }
  }

  public count(): number {
    return this.length;
  }
}
