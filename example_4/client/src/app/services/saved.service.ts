import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable()
export class GetSavedOperationService {

  constructor(private http: HttpClient) { }

  getSaved(id:number) : Observable<Result> {
    const baseUrl = `${environment.apiUrl}/${id}`;

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
