#include <stdio.h>
#include <stdlib.h>

struct Node{
    int value;
    struct Node* next;
};

struct LinkedList{
    struct Node* head;
    struct Node* tail;
};

struct LinkedList createList(){
    printf("Creating LinkedList\n");
    struct LinkedList list;
    list.head = NULL; // Initialize head to NULL
    list.tail = NULL; // Initialize head to NULL
    return list;
}

void append(struct LinkedList* list, int num){
    struct Node* node = malloc(sizeof(struct Node)); // Dynamically allocate memory
    node->value = num;
    node->next = NULL;

    // printf("Appending %d to LinkedList\n", num);

    if (list->head == NULL){
        list->head = node;
        list->tail = node;
    } else {
        list->tail->next = node;
        list->tail = node;
    }
}

void print(struct LinkedList* list){
    struct Node* curr = list->head;
    printf("Printing Linked List...\n");
    while (curr != NULL){
        printf("%d\n", curr->value);
        curr = curr->next;
    }
}

int main(){
    struct LinkedList list = createList();

    for (int i = 0; i< 1000000;i++){
      append(&list, i);
    }
    print(&list); 


    printf("Freeing Memory\n");
    struct Node* curr = list.head;
    while (curr != NULL) {
        struct Node* temp = curr;
        curr = curr->next;
        free(temp);
    }

}
