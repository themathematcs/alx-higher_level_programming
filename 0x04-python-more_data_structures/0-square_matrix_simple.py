#!/bin/bash

def square_matrix_simple(matrix[]):
     if matrix:
           new = []
           for rows in matrix:
                 new.append([n ** 2 for n in rows])
            return new
