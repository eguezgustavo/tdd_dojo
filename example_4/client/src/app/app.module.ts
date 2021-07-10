import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { OperationService } from './services/operations.service';
import { DoOperationService } from './services/operation.service';
import { GetSavedOperationService } from './services/saved.service';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
  ],
  providers: [
    OperationService,
    DoOperationService,
    GetSavedOperationService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
