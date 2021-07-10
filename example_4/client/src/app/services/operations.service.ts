import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable()
export class OperationService {



  constructor(private http: HttpClient) { }
  baseUrl = `${environment.apiUrl}/operations`;

  getOperations() : Observable<Operation[]> {
    return this.http.get<Operation[]>(this.baseUrl)
  }
}

export interface Operation {
  id: number;
  name: string;
}
