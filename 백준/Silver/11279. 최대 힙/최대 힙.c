#include <stdio.h>
#include <stdlib.h>

#define MAX_ELEMENTS 101010 /* maximum size of heap+1 */
#define HEAP_FULL(n) (n == MAX_ELEMENTS-1)
#define HEAP_EMPTY(n) (!n)

typedef struct {
    int key;
} element;

void heap_push();
element heap_pop();
void heap_up();
void heap_down();
void heap_swap();

int n = 0;

element heap[MAX_ELEMENTS];

void heap_push(int key){
    if (n + 1 == MAX_ELEMENTS){
        printf("The heap is full. ");
        exit(0);
    }
    heap[++n].key = key;
    heap_up(n);
}

element heap_pop(){
    if (n == 0){

        element x;
        x.key = 0;
        return x;

        printf("The heap is empty. ");
        exit(0);
    }

    element top = heap[1];
    heap_swap(1, n--);
    heap_down(1);

    return top;
}

void heap_up(int pos){
    if (pos == 1) return;

    int par_pos = pos/2;
    if (heap[par_pos].key < heap[pos].key){
        heap_swap(par_pos, pos);
        heap_up(par_pos);
    }
}

void heap_down(int pos){
    int left_pos = pos * 2;
    int right_pos = pos * 2 + 1;
    int next_pos;

    if (left_pos <= n && right_pos <= n){
        if (heap[left_pos].key < heap[right_pos].key){
            next_pos = right_pos;
        } else {
            next_pos = left_pos;
        }
    } else if (left_pos <= n){
        next_pos = left_pos;
    } else {
        return;
    }

    if (heap[next_pos].key > heap[pos].key){
        heap_swap(pos, next_pos);
        heap_down(next_pos);
    }
}

void heap_swap(int pos1, int pos2){
    element tmp = heap[pos1];
    heap[pos1] = heap[pos2];
    heap[pos2] = tmp;
}


int main(){
    // heap_push(5);
    // heap_push(7);
    // heap_push(1);
    // heap_push(2);
    // heap_push(4);
    // heap_push(10);
    // heap_push(8);
    // element p = heap_pop();
    // printf("%d\n", p.key);

    // for (int i = 1; i <= n; i++) printf("%d ", heap[i].key);

    int t; scanf("%d", &t);

    for (int i = 0; i < t; i++){
        int x; scanf("%d", &x);
        if (x) heap_push(x);
        else printf("%d\n", heap_pop().key);

        // for (int j = 1; j <= n; j++) printf("%d ", heap[j].key);
        // printf("\n");
    }

    return 0;
}