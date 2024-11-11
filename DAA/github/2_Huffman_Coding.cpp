#include<bits/stdc++.h>

using namespace std;

struct MinHeapNode{
	char data;
	int freq;
	MinHeapNode* left, *right;
	MinHeapNode(char data, int freq){
		left=right=nullptr;
		this->data = data;
		this->freq = freq;
	}
};


void printCodes(struct MinHeapNode* root, string str){
	if(root == nullptr){
		return;
	}
	if(root->data != '$'){
		cout << root->data << ": " << str << endl;
	}
	printCodes(root->left, str + "0");
	printCodes(root->right, str + "1");
}

struct compare{
	bool operator()(MinHeapNode* a, MinHeapNode* b){
		return (a->freq > b->freq);
	}
};

void HuffmanCode(char data[], int freq[], int size){
	struct 	MinHeapNode *left, *right, *temp;
	
	priority_queue<MinHeapNode*, vector<MinHeapNode*>, compare> minHeap;
	
	for(int i = 0; i < size; i++){
		minHeap.push(new MinHeapNode(data[i], freq[i]));
	}
	
	while(minHeap.size() != 1){
		left = minHeap.top();
		minHeap.pop();
		right = minHeap.top();
		minHeap.pop();
		temp = new MinHeapNode('$', left->freq + right->freq);
		temp->left = left;
		temp->right = right;
		minHeap.push(temp);
	}
	printCodes(minHeap.top(), "");
}


int main(){
	char data[] = {'A', 'B', 'C', 'D'};
	int freq[] = {23,12,34,10};
	HuffmanCode(data, freq, 4);
	return 0;
}

/*
Huffman Coding :
Time complexity: O(nlogn) where n is the number of unique characters.
If there are n nodes, extractMin() is called 2*(n – 1) times. extractMin() takes O(logn) time as it calls minHeapify(). So, overall complexity is O(nlogn).
*/




//chatgpt code with better readability 
#include <bits/stdc++.h>
using namespace std;

struct MinHeapNode {
    char data;
    int freq;
    MinHeapNode* left, *right;
    MinHeapNode(char data, int freq) {
        left = right = nullptr;
        this->data = data;
        this->freq = freq;
    }
};

void printCodes(MinHeapNode* root, const string& str) {
    if (root == nullptr) return;
    if (root->data != '$') {
        cout << root->data << ": " << str << endl;
    }
    printCodes(root->left, str + "0");
    printCodes(root->right, str + "1");
}

struct compare {
    bool operator()(MinHeapNode* a, MinHeapNode* b) {
        return a->freq > b->freq;
    }
};

void HuffmanCode(const vector<char>& data, const vector<int>& freq, int size) {
    if (size == 0) {
        cout << "No data to encode!" << endl;
        return;
    }

    priority_queue<MinHeapNode*, vector<MinHeapNode*>, compare> minHeap;

    for (int i = 0; i < size; i++) {
        minHeap.push(new MinHeapNode(data[i], freq[i]));
    }

    while (minHeap.size() != 1) {
        MinHeapNode* left = minHeap.top(); minHeap.pop();
        MinHeapNode* right = minHeap.top(); minHeap.pop();

        MinHeapNode* temp = new MinHeapNode('$', left->freq + right->freq);
        temp->left = left;
        temp->right = right;
        minHeap.push(temp);
    }

    printCodes(minHeap.top(), "");
}

int main() {
    vector<char> data = {'A', 'B', 'C', 'D'};
    vector<int> freq = {23, 12, 34, 10};
    
    if (data.size() != freq.size()) {
        cout << "Error: Data and frequency arrays have different sizes." << endl;
        return 1;
    }
    
    HuffmanCode(data, freq, data.size());
    
    return 0;
}
