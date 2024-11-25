//
//  Gestionnaire.cpp
//
//  Created by Ingenuity i/o on 2024/10/18.
//  Copyright © 2023 Ingenuity i/o. All rights reserved.
//

#include "Gestionnaire.h"


Gestionnaire::Gestionnaire()
    : _newAttributeA(false)
{
}

Gestionnaire::~Gestionnaire(){
}

/////////////////////////////////////////////////////////////////////
//inputs
// demande
void Gestionnaire::setDemandeI()
{

    //add code here if needed

}

/////////////////////////////////////////////////////////////////////
//outputs
// carte
void Gestionnaire::setCarteO()
{

    //add code here if needed

    igs_output_set_impulsion("carte");
}

/////////////////////////////////////////////////////////////////////
//attributes
// new_attribute
void Gestionnaire::setNewAttributeA(bool value)
{
    _newAttributeA = value;

    //add code here if needed

}
bool Gestionnaire::getNewAttributeA() const
{

    //add code here if needed

    return _newAttributeA;
}


/////////////////////////////////////////////////////////////////////
//services
void Gestionnaire::donnerCarte(bool joueur){

    //add code here if needed

}

