#!/usr/bin/env python3

import argparse
import timewatch


def main(company, employee_id, password, option):
    client = timewatch.TimeWatch(company, employee_id, password)
    client.login()
    if option == 'in':
        client.punch_in()
    elif option == 'out':
        client.punch_out()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Punch in time to timewatch')
    parser.add_argument('--company', '-c',
                        help='Company ID', type=int, required=True)
    parser.add_argument('--employee-id', '-e',
                        help='Employee ID', type=int, required=True)
    parser.add_argument('--password', '-p',
                        help='Password for logging in', required=True)
    parser.add_argument('--option', '-o', required=True, choices=['in', 'out'])
    args = parser.parse_args()
    main(args.company, args.employee_id, args.password, args.option)
