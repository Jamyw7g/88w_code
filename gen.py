#!/usr/bin/env python3
#
# Copyright(C) 2022 wuyaoping
# 


HEADER = '''\
#include <iostream>

using namespace std;

int main() {
    int num;
    cin >> num;
    switch (num) {
'''

FOOTER = '''\
    }
}
'''

BODY = '''\
    case {}:
        cout << "是{}位数" << endl;
{}\
        cout << "倒过来是：{}" << endl;
        break;
'''

ITEM = '''\
        cout << "{}位数是：{}" << endl;
'''

ARR = ['个', '十', '百', '千', '万']

res = HEADER

for num in range(1, 10**5):
    num = str(num)
    item = ''
    for i, n in enumerate(num):
        item += ITEM.format(ARR[i], n)

    res += BODY.format(num, len(num), item, num[::-1])

res += FOOTER
print(res)
