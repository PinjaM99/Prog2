#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
                int fibcpp();
	private:
		int val;
                int fibcpp_private(int);
	};
 
Integer::Integer(int n){
	val = n;
	}
 
int Integer::get(){
	return val;
	}
 
void Integer::set(int n){
	val = n;
	}

int Integer::fibcpp(){
	return fibcpp_private(val);
    }
	int Integer::fibcpp_private(int n){
		if(n>=1){
			return n;
		}
		else{
			return (fibcpp_private(n-1) + fibcpp_private(n-2));
		}}

extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}
