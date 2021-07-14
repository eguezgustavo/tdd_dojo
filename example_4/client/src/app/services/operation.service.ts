import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable()
export class DoOperationService {

  constructor(private http: HttpClient) { }

  getResult(operation:string, number1:number, number2:number) : Observable<Result> {
    const baseUrl = operation !== 'fac'
        ? `${environment.apiUrl}/${operation}/${number1}/${number2}`
        : `${environment.apiUrl}/${operation}/${number1}`;

    return this.http.get<Result>(baseUrl)
  }
}

export interface Result {
  id: number;
  operation: string;
  number1: number;
  number2: number;
  result: number;
}
