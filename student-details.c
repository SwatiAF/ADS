/*list of students with details
-->name 
-->usn
-->subject 
-->marks 

sort the list 

create another list for failed students -- > check the list for failing students and create a 
new list using a function

let the passing marks be 60
*/

#include<stdio.h>
#include<stdlib.h>

int i, j;

struct node {
    char name[20];
    int usn;
    char subject[10];
    int marks[10];
    struct node *next;
};
struct node *head;

void insertAtEnd() {
    struct node *ptr, *temp;
    int usn;
    char name;
    char subject;
    int marks;
    ptr = (struct node *)malloc(sizeof(struct node *));
    if(ptr == NULL) {
        printf("Queue Full\n");
    }
    else {
        printf("Enter USN of the student: ");
        scanf("%d", &usn);
        ptr->usn = usn;
        
        printf("Enter name: ");
        scanf("%s", ptr->name);
        ptr->name[20] = name;
            
        for(i = 0; i < 10; i++) {
            printf("Enter subject %d: ", i);
            scanf("%s", ptr->subject[i]);
            ptr->subject[i] = subject;
        }
        
        for(j = 0; j < 10; j++) {
            printf("Enter marks for subject %d: ", i);
            scanf("%d", ptr->marks[j]);
            ptr->marks[j] = marks;
        }
        
        if(head == NULL) {
            ptr->next = NULL;
            head = ptr;
            printf("Node inserted\n");
        }
        else {
            temp = head;
            while(temp->next != NULL) {
                temp = temp->next;
            }
            temp->next = ptr;
            ptr->next = NULL;
            printf("Node inserted\n");
        }
    }
}

void display() {
    struct node *ptr;
    ptr = (struct node *)malloc(sizeof(struct node *));
    ptr = head;
    if(head == NULL) {
        printf("List empty\n");
    }
    else {
        printf("List: \n");
        while(ptr != NULL) {
            printf("%d \n", ptr->usn);
            printf("%s \n", ptr->name);
            
            for(i = 0; i < 10; i++) {
                printf("%s \n", ptr->subject);
            }
            
            for(j = 0; j < 10; j++) {
                printf("%d \n", ptr->marks);
            }
            ptr = ptr->next;
        }
    }
}

void sort_list() {
    /*sort the list based on total marks*/
    
}

void failed_list() {
    /*check for failed students where total marks < 60 and create a list for the failed students*/
}

void main() {
    int choice;
    while(1) {
        printf("Insertion Operations: \n");
        printf("1.Insert at end\n 2.Display\n 3.Sort based on Total Marks\n 4.Check & create for failed\n 5.Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);
        
        switch(choice) {
            case 1: insertAtEnd();
                break;
            case 2: display();
                break;
            case 3: sort_list();
                break;
            case 4: failed_list();
                break;
            case 5: exit(1);
                break;
            default: printf("Invalid Choice");
        }
    }
}



