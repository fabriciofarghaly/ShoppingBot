//
//  StoreItem.swift
//  ShoppingBot
//
//  Created by Charlie Mulholland on 11/28/22.
//

import Foundation


class StoreItem {
    let id: String
    let price: Float
    let name: String?
    
    
    init(id: String, price: Float, name: String?) {
        self.id = id
        self.price = price
        self.name = name ?? nil
    }
}

