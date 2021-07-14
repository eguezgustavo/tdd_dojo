import { Component } from '@angular/core';
import { DoOperationService, Result } from './services/operation.service';
import { GetSavedOperationService } from './services/saved.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent{
  endpointSelected: string = '1';
  operationSelected: string = 'sum';
  response;
  result: Result;
  title = 'client';
  number1: number;
  number2: number;
  id: number;
  endpoints = [
    {value: '1', viewValue: 'Do operation'},
    {value: '2', viewValue: 'Element from history'}
  ]

  operations = [
    {value: '1', viewValue: 'sum'},
    {value: '2', viewValue: 'sub'},
    {value: '3', viewValue: 'fac'}
  ]

  constructor(
    private doOperationService: DoOperationService,
    private getSavedOperationService: GetSavedOperationService
  ) { }
  ngOnInit() {
  }

  changeOption(event) {
    this.endpointSelected = event.target.value;
  }

  changeOperation(event) {
    this.operationSelected = event.target.value;
  }

  onSendRequest() {
    if(this.endpointSelected == '1'){
      this.doOperation()
    }
    if(this.endpointSelected == '2'){
      this.getSavedOperation()
    }
  }

  doOperation(): void {
    this.doOperationService.getResult(
      this.operationSelected,
      this.number1,
      this.number2
    )
      .subscribe(operations =>{
        this.result = operations
      });
  }

  getSavedOperation(): void {
    this.getSavedOperationService.getSaved(
      this.id,
    )
      .subscribe(operations =>{
        this.result = operations
      });
  }
}
