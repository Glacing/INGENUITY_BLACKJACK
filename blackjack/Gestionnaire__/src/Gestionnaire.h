//
//  Gestionnaire.h
//  Created by Ingenuity i/o on 2024/10/18
//
//  no description
//  Copyright © 2023 Ingenuity i/o. All rights reserved.
//
#ifndef Gestionnaire_h
#define Gestionnaire_h

#ifdef INGESCAPE_FROM_PRI
#include "ingescape.h"
#else
#include <ingescape/ingescape.h>
#endif // INGESCAPE_FROM_PRI

#include <string>

class Gestionnaire {
public:
    Gestionnaire();
    ~Gestionnaire();

    //inputs
    void setDemandeI();

    //outputs
    void setCarteO();

    //attributes
    void setNewAttributeA(bool value);
    bool getNewAttributeA() const;

    //services
    void donnerCarte(bool joueur);

private:
    //inputs

    //outputs

    //attributes
    bool _newAttributeA;

};

#endif /* Gestionnaire_h */
