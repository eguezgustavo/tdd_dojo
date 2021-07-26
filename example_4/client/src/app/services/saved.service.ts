import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { AppConfigService } from './config.service';

@Injectable()
export class GetSavedOperationService {
  basePath: string;

  constructor(private environment: AppConfigService, private http: HttpClient) {
    this.basePath = environment.config.apiUrl;
  }

  getSaved(id:number) : Observable<Result> {
    const baseUrl = `${this.basePath}/${id}`;

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
